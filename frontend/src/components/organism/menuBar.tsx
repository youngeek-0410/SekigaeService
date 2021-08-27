import * as React from "react"
import { css } from "@emotion/react"

import StartButton from "components/atom/startButton"
import AskButton from "components/atom/askButton"

const MenuBar: React.FC<{}> = () => {
  return (
    <div
      css={css({
        position: "fixed",
        width: "90vw",
        height: "120px",
        left: "5vw",
        top: "2vw",

        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",

        background: "rgba(255, 255, 255, 0.5)",
        boxShadow: "4px 4px 4px rgba(0,0,0,0.25)",
        backdropFilter: "blur(10px)",

        borderRadius: "16px",
      })}><div css={css({
        width:"100%",
        paddingInline:"2rem",

        display: "flex",
        justifyContent:"space-between",
        alignItems:"center",
      })}>
        <p css={css({
          color: "white",
          fontFamily: "Merge One",
          fontStyle: "normal",
          fontWeight: "normal",
          fontSize: "min(5vw,100px)",
          display:"inline",
          whiteSpace: "nowrap",
        })}>[App name]</p>
        <div css={css({
          display:"flex",
        })}>
          <div css={css({marginInline:"2rem"})}><StartButton /></div>
          <div css={css({marginInline:"2rem"})}><AskButton /></div>
          <svg xmlns="http://www.w3.org/2000/svg" width="72" height="72" fill="currentColor" className="bi bi-list" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z" />
          </svg>
          </div>
      </div>
    </div>
  )
}

export default MenuBar