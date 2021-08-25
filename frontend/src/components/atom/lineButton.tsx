/** @jsx jsx */
<<<<<<< Updated upstream:frontend/src/components/atom/lineButton.tsx
import { jsx } from "@emotion/react"
import { css } from "@emotion/react"

//注意！onClickの型はどんな関数を入れるか定まっていないのでany
interface Props{
  text: string
  onClick?: any
=======
import * as React from "react"

import { jsx } from "@emotion/react"
import { css } from "@emotion/react"

interface Props{
  text: string
  onClick?: (event: React.MouseEvent<HTMLInputElement>)=> void
>>>>>>> Stashed changes:frontend/src/components/atom/LineButton.tsx
}

const LineButton: React.FC<Props> = ({text,onClick}) => {
  return (
<<<<<<< Updated upstream:frontend/src/components/atom/lineButton.tsx
    <div onClick={onClick}
=======
    <button onClick={onClick}
>>>>>>> Stashed changes:frontend/src/components/atom/LineButton.tsx
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
<<<<<<< Updated upstream:frontend/src/components/atom/lineButton.tsx
      })}>{text}</div>
=======
      })}>{text}</button>
>>>>>>> Stashed changes:frontend/src/components/atom/LineButton.tsx
  )
}

export default LineButton