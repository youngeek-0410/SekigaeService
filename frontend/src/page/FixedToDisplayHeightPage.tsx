import { Box } from "@chakra-ui/layout"
import Header from "common/components/Header"

const FixedToDisplayHeightPage = () => {
  return (
    <Box height="100vh">
      <Header />
      <p>This page height is fixed.</p>
    </Box>
  )
}

export default FixedToDisplayHeightPage