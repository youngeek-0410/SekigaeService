import { css } from "@emotion/react"

const LineButton: React.FC<React.ButtonHTMLAttributes<HTMLButtonElement>> = props => {
  return (
    <button onClick={props.onClick}
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
      })}>{props.children}</button>
  )
}

export default LineButton