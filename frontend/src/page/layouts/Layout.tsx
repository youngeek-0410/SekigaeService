import { ReactNode } from "react"

import Header from "common/components/Header"

type Props = {
  children: ReactNode;
}

export function Layout({ children }: Props) {
  return (
    <>
      <Header />
      {children}
    </>
  )
}