local hovered = ya.sync(function()
  local h = cx.active.current.hovered
  return h and tostring(h.url)
end)

return {
  entry = function()
    local path = hovered()
    if not path then return end
    local output, err = Command("/bin/zsh")
      :arg(os.getenv("HOME") .. "/.config/agterm/scripts/yazi-insert-path.zsh")
      :arg(path)
      :output()
    if output and output.status.success then
      ya.emit("quit", {})
    else
      ya.notify { title = "Insert path", content = output and output.stderr or tostring(err), level = "error", timeout = 5 }
    end
  end,
}
