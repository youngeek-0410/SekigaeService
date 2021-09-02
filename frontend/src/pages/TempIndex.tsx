import * as React from "react"
import ReactDOM from "react-dom"

import { Button } from "@material-ui/core"

const TempIndex: React.FC = () => {
  return (
    <Button
      variant="contained"
      color="primary"
    >Hello, Material-UI!</Button>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <TempIndex />
  </React.StrictMode>,
  document.getElementById('app')
)