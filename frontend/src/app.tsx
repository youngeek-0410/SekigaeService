import React from 'react'
import ReactDOM from 'react-dom'

import Top from 'pages/sekigae'

const App: React.FC<{}> = () => {
    return(
        <>
            <Top />
        </>
    )
}

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('app')
)