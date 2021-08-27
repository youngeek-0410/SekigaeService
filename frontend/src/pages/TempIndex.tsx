import * as React from "react"
import ReactDOM from "react-dom"

import Header from "components/organism/Header"

const TempIndex:React.FC=()=>{
  return(
    <Header/>
  )
}

ReactDOM.render(
  <React.StrictMode>
      <TempIndex />
  </React.StrictMode>,
  document.getElementById('app')
)