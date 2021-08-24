/** @jsx jsx */
import { jsx } from "@emotion/react"
import { css } from "@emotion/react"

const StartButton = () => {
  return (
    <div
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
      })}
    ><p>席替えを始める</p></div>
  )
}

export default StartButton