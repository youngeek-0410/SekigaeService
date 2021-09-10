import { css } from "@emotion/react"

const FilledButton: React.FC<React.ButtonHTMLAttributes<HTMLButtonElement>> = props => {
  return (
    <button onClick={props.onClick}
      css={css({
        color:"white",
        fontSize:"18px",

        width: "250px",
        height: "72px",

        textAlign:"center",
        lineHeight:"72px",

        backgroundColor: "rgba(96,168,176,0.75)",
        boxShadow: "4px 4px 4px rgba(0,0,0,0.25)",
        border:"none",
        borderRadius: "8px",
        userSelect:"none",
      })}>{props.children}</button>
  )
}

export default FilledButton