function ancient_search(input, seg)
    if #input > 0 then
       local handle = io.popen("~/.venv/bin/python /home/ytsun/Documents/3.1/Chinese_Toolbook/gujizhilian/search/search.py " .. input)
       local result = handle:read("*a")
       handle:close()
 
       local candidates = {}
       for line in string.gmatch(result, "[^\r\n]+") do
           table.insert(candidates, line)
       end
 
       for i, candidate in ipairs(candidates) do
          yield(Candidate("text", seg.start, seg._end, candidate, "出處"))
       end
    end
 end