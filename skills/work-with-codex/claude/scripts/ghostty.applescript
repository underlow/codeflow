on run argv
    set op to item 1 of argv
    tell application "Ghostty"
        if op is "identify" then
            -- Snapshot titles before the temporary marker changes the parent's title.
            set originals to {}
            repeat with w in windows
                repeat with parentTab in tabs of w
                    repeat with t in terminals of parentTab
                        set end of originals to {id of t, name of t, name of parentTab}
                    end repeat
                end repeat
            end repeat
            set ttyPath to item 2 of argv
            set marker to item 3 of argv
            do shell script "/usr/bin/printf '\\033]2;%s\\007' " & quoted form of marker & " > " & quoted form of ttyPath
            repeat 20 times
                repeat with w in windows
                    repeat with t in terminals of w
                        if name of t is marker then
                            repeat with original in originals
                                if item 1 of original is (id of t) then
                                    do shell script "/usr/bin/printf '\\033]2;%s\\007' " & quoted form of (item 2 of original) & " > " & quoted form of ttyPath
                                    return (id of t) & linefeed & (item 3 of original)
                                end if
                            end repeat
                        end if
                    end repeat
                end repeat
                delay 0.1
            end repeat
            error "cannot find the originating terminal in Ghostty"
        end if
        if op is "find-title" then
            repeat with w in windows
                repeat with t in terminals of w
                    if name of t is (item 2 of argv) then return id of t
                end repeat
            end repeat
            return ""
        end if
        -- Resolve by id on every call: tabs move between windows and change index.
        set target to missing value
        set targetWindow to missing value
        repeat with w in windows
            repeat with t in terminals of w
                if id of t is (item 2 of argv) then
                    set target to contents of t
                    set targetWindow to contents of w
                end if
            end repeat
        end repeat
        if op is "exists" then return target is not missing value
        if target is missing value then error "terminal " & (item 2 of argv) & " not found"
        if op is "tab" then
            set parentTitle to item 5 of argv
            set takenTitles to name of every tab of targetWindow
            set childNumber to 1
            set childTitle to "(" & childNumber & ") " & parentTitle
            repeat while takenTitles contains childTitle
                set childNumber to childNumber + 1
                set childTitle to "(" & childNumber & ") " & parentTitle
            end repeat
            set cfg to new surface configuration
            set command of cfg to item 3 of argv
            set initial working directory of cfg to item 4 of argv
            set wait after command of cfg to true
            set newTab to new tab in targetWindow with configuration cfg
            perform action ("set_tab_title:" & childTitle) on focused terminal of newTab
            return id of focused terminal of newTab
        else if op is "input" then
            input text (item 3 of argv) to target
        else if op is "key" then
            send key (item 3 of argv) to target
        else if op is "focus" then
            focus target
        else if op is "close" then
            close target
        end if
        return "ok"
    end tell
end run
