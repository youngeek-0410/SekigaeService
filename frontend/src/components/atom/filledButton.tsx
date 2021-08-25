/** @jsx jsx */
<<<<<<< Updated upstream:frontend/src/components/atom/filledButton.tsx
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
>>>>>>> Stashed changes:frontend/src/components/atom/FilledButton.tsx
}

const FilledButton: React.FC<Props> = ({text,onClick}) => {
  return (
<<<<<<< Updated upstream:frontend/src/components/atom/filledButton.tsx
    <div onClick={onClick}
=======
    <button onClick={onClick}
>>>>>>> Stashed changes:frontend/src/components/atom/FilledButton.tsx
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
<<<<<<< Updated upstream:frontend/src/components/atom/filledButton.tsx
      })}
    ><p>{text}</p></div>
=======
      })}>{text}</button>
>>>>>>> Stashed changes:frontend/src/components/atom/FilledButton.tsx
  )
}

export default FilledButton