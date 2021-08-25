/** @jsx jsx */
import * as React from "react"

import { jsx } from "@emotion/react"
import { css } from "@emotion/react"

interface Props{
  text: string
  onClick?: (event: React.MouseEvent<HTMLInputElement>)=> void
}

const LineButton: React.FC<Props> = ({text,onClick}) => {
  return (
    <button onClick={onClick}
      css={css({
        color:"white",
        fontSize:"18px",

        width: "250px",
        height: "72px",

        textAlign:"center",
        lineHeight:"72px",

        backgroundColor: "rgba(0,0,0,0)",
        boxSizing: "border-box",
        border: "1px solid #FFFFFF",
        borderRadius: "8px",
        userSelect:"none",
      })}>{text}</button>
  )
}

export default LineButton