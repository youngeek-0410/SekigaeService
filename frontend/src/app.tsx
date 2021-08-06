import React from 'react'
import ReactDOM from 'react-dom'

import HelloWorld from './HelloWorld'

const App: React.FC = () => {
    return(
        <div>
            <p>hi</p>
            <HelloWorld />
        </div>
    )
}

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('app')
)