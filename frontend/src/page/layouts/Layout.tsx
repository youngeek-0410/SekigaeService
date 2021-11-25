import { ReactNode } from 'react'

type Props = {
  children: ReactNode;
}

export function Layout({ children }: Props) {
  return (
    <>
      <p>this is header</p>
      {children}
    </>
  )
}