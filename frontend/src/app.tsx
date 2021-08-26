import React from "react"
import ReactDOM from "react-dom"

import Top from "pages/Top"
import Header from "components/organism/Header"

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
