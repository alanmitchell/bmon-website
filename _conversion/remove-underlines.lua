function Span(elem)
    -- If the span contains an underline class, remove the span and keep the content
    if elem.classes:includes("underline") then
      return elem.content
    else
      -- Else, leave the span as is
      return elem
    end
  end
  