// Keep a console window from opening on Windows release builds.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::ipc::{InvokeBody, Request};
use tauri::menu::{Menu, MenuItem, PredefinedMenuItem, Submenu};
use tauri_plugin_dialog::DialogExt;

const APP_NAME: &str = "Kero's SE WevMac";

// Undo encodeURIComponent, which the page uses to get a file name through an HTTP header.
fn percent_decode(s: &str) -> String {
    let b = s.as_bytes();
    let mut out = Vec::with_capacity(b.len());
    let mut i = 0;
    while i < b.len() {
        if b[i] == b'%' && i + 2 < b.len() && s.is_char_boundary(i + 1) && s.is_char_boundary(i + 3) {
            if let Ok(v) = u8::from_str_radix(&s[i + 1..i + 3], 16) {
                out.push(v);
                i += 3;
                continue;
            }
        }
        out.push(b[i]);
        i += 1;
    }
    String::from_utf8_lossy(&out).into_owned()
}

// The page sends the disk image as the raw request body. Ask where to put it and write it there.
// Returns the path, or None if the user cancelled.
#[tauri::command]
async fn save_disk(app: tauri::AppHandle, request: Request<'_>) -> Result<Option<String>, String> {
    let InvokeBody::Raw(bytes) = request.body() else {
        return Err("no disk data was sent".into());
    };
    let name = request
        .headers()
        .get("x-file-name")
        .and_then(|v| v.to_str().ok())
        .map(percent_decode)
        .unwrap_or_else(|| "disk.dsk".into());

    let Some(choice) = app.dialog().file().set_file_name(name).blocking_save_file() else {
        return Ok(None);
    };
    let path = choice.into_path().map_err(|e| e.to_string())?;
    std::fs::write(&path, bytes).map_err(|e| e.to_string())?;
    Ok(Some(path.display().to_string()))
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_opener::init())
        .menu(|handle| {
            // Quit has no Command-Q shortcut, and there are no Edit or Window menus, so that
            // Command key shortcuts reach the emulated Mac instead of this app.
            let quit = MenuItem::with_id(handle, "quit", format!("Quit {APP_NAME}"), true, None::<&str>)?;
            let app_menu = Submenu::with_items(
                handle,
                APP_NAME,
                true,
                &[
                    &PredefinedMenuItem::about(handle, None, None)?,
                    &PredefinedMenuItem::separator(handle)?,
                    &quit,
                ],
            )?;
            Menu::with_items(handle, &[&app_menu])
        })
        .on_menu_event(|app, event| {
            if event.id() == "quit" {
                app.exit(0);
            }
        })
        .invoke_handler(tauri::generate_handler![save_disk])
        .run(tauri::generate_context!())
        .expect("error while running the app");
}
