/** @jsx jsx */
import * as React from "react"
import { jsx } from "@emotion/react"
import { css } from "@emotion/react"

const AskButton: React.FC = (prop) => {
  return (
    <div
      css={css({
        color:"white",
        fontSize:"18px",

        width: "250px",
        height: "72px",

        textAlign:"center",
        lineHeight:"72px",

        border: "1px solid #FFFFFF",
        boxSizing: "border-box",
        borderRadius: "8px",
      })}>お問い合わせ</div>
  )
}

export default AskButton