import { css } from "@emotion/react"

//注意！onClickの型はどんな関数を入れるか定まっていないのでany
interface Props{
  text: string
  onClick?: any
}

const LineButton: React.FC<Props> = ({text,onClick}) => {
  return (
    <div onClick={onClick}
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
        userSelect:"none",
      })}>{text}</div>
  )
}

export default LineButton