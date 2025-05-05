import { action, KeyDownEvent, SingletonAction } from "@elgato/streamdeck";
import { exec } from "child_process";

@action({ UUID: "com.canaryknight.macos-binings.spotlight" })
export class SpotlightAction extends SingletonAction<{}> {
    override async onKeyDown(ev: KeyDownEvent<{}>): Promise<void> {
        exec(`osascript -e 'tell application "System Events" to key code 49 using {command down, option down}'`);
    }
}
