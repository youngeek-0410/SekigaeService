import React from "react"
import ReactDOM from "react-dom"

import Top from "pages/sekigae"
import Header from "components/organism/header"

const headerElement = document.getElementById("header")
if (headerElement) {
  ReactDOM.render(
    <React.StrictMode>
      <Header />
    </React.StrictMode>,
    headerElement
  )
}

const topElement = document.getElementById("top")
if (topElement) {
  ReactDOM.render(
    <React.StrictMode>
      <Top />
    </React.StrictMode>,
    topElement
  )
}
