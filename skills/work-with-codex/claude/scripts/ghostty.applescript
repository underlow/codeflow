on run argv
    set op to item 1 of argv
    tell application "Ghostty"
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
            set cfg to new surface configuration
            set command of cfg to item 3 of argv
            set initial working directory of cfg to item 4 of argv
            set wait after command of cfg to true
            set newTab to new tab in targetWindow with configuration cfg
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
