import { action, KeyDownEvent, SingletonAction } from "@elgato/streamdeck";
import { exec } from "child_process";

@action({ UUID: "com.canaryknight.macos-binings.lock" })
export class LockAction extends SingletonAction<{}> {
    override async onKeyDown(ev: KeyDownEvent<{}>): Promise<void> {
        exec("pmset displaysleepnow", (error, stdout, stderr) => {
            if (error) {
                console.error("Failed to put display to sleep:", stderr);
            }
        });
    }
}
