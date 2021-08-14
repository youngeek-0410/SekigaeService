/** @jsx jsx */
import * as React from 'react'
import { jsx } from '@emotion/react'
import { css } from '@emotion/react'

const HelloWorld: React.FC = () => {
    return(
        <div css={css({
            backgroundColor:'aqua'
        })}>
            <p>Hello, World!!!!</p>
        </div>
    )
}
export default HelloWorld