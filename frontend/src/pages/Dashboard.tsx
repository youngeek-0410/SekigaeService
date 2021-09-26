import ReactDOM from "react-dom"
import * as React from "react"
import { useState } from "react"

import { css } from "@emotion/react"

import Box from "@mui/material/Box"
import Button from "@mui/material/Button"
import { Stepper, Step, StepLabel, StepContent } from "@mui/material"
import { Typography } from "@mui/material"

import Header from "components/organism/Header"
//import FrontSheets from "components/organism/FrontSheets"
//import StudentSheet from "components/organism/StudentSheet"
//import SeatFormats from "components/organism/SeatFormats"

//名簿選択、前席の指定、座席の形を順番に決めるUI
//mUIのStepperをメインに使うコンポーネント(ページ)になる。

//stepの説明
const getSteps = () => {
  return ([
    "クラスの名簿を決める",
    "前方の座席の人を決める",
    "座席の並んでいる形を決める",
    "席替えする！"
  ])
}

const getStepContent = (step: number) => {
  switch (step) {
    case 0:
      return (
        <div
          css={css({
            height: "400px",
          })}
        ><p>名簿選択</p></div>
      )
    case 1:
      return (
        <div
          css={css({
            height: "400px",
          })}
        ><p>前席選択</p></div>
      )
    case 2:
      return (
        <div
          css={css({
            height: "400px",
          })}
        ><p>座席の形選択</p></div>
      )
    case 3:
      return (
        <Typography>席替えする！</Typography>
      )
    default:
      return <Typography>unknown step</Typography>
  }
}

const Dashboard: React.FC = () => {
  const [activeStep, setActiveStep] = useState(0)
  const steps = getSteps()

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  }

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  }

  return (
    <Box sx={{ ml: 1, mr: 1 }}>
      <Stepper activeStep={activeStep} orientation="vertical">
        {steps.map((label, index) => (
          <Step key={label}>
            <StepLabel>{label}</StepLabel>
            <StepContent>
              <div>
                {getStepContent(index)}
              </div>
              <Box sx={{ mb: 2 }}>
                <div>
                  <Button
                    disabled={activeStep === 0}
                    onClick={handleBack}
                  >
                    Back
                  </Button>
                  {/* stepが最後のとき、表示されないようにする*/}
                  <Button
                    disabled={activeStep === steps.length - 1}
                    variant="contained"
                    color="primary"
                    onClick={handleNext}
                    sx={{ mt: 1, mr: 1 }}
                  >
                    Next
                  </Button>
                  {/* 席替えするボタンは最後にならないと出ない */
                    (activeStep === steps.length - 1) &&
                    <Button
                      disabled={activeStep !== steps.length - 1}
                      variant="contained"
                      color="primary"
                      sx={{ mt: 1, mr: 1 }}
                    >
                      席替えする!
                    </Button>
                  }
                </div>
              </Box>
            </StepContent>
          </Step>
        ))}
      </Stepper>
    </Box>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <div
      css={css({
        height: "100%"
      })}
    >
      <Header />
      <Dashboard />
    </div>
  </React.StrictMode>,
  document.getElementById('app')
)