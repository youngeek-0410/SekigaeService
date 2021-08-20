/** @jsx jsx */
import * as React from "react"
import { jsx } from "@emotion/react"
import { css } from "@emotion/react"

//注意！onClickの型はどんな関数を入れるか定まっていないのでany
interface Props{
  text: string
  onClick?: any
}

const FilledButton: React.FC<Props> = ({text,onClick}) => {
  return (
    <div onClick={onClick}
      css={css({
        color:"white",
        fontSize:"18px",

        width: "250px",
        height: "72px",

        textAlign:"center",
        lineHeight:"72px",

        backgroundColor: "rgba(96,168,176,0.75)",
        boxShadow: "4px 4px 4px rgba(0,0,0,0.25)",
        borderRadius: "8px",
        userSelect:"none",
      })}
    ><p>{text}</p></div>
  )
}

export default FilledButton