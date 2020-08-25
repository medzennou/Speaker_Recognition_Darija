import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"

import Styles from './stream.module.css'
import img from './Contact-Us-lines-2.png'

interface State {
  numClicks: number
}

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class MyComponent extends StreamlitComponentBase<State> {
  public state = { numClicks: 0 }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
   // const name = this.props.args["nom"]

    // Show a button and some text.
    // When the button is clicked, we'll increment our "numClicks" state
    // variable, and send its new value back to Streamlit, where it'll
    // be available to the Python program.
    return (  
      <div>
     
      <img className={Styles.imag} src={img} height="100" width="550" />
      <h5 className={Styles.hema}>Speaker Recognition HENCEFORTH</h5>
  
      </div>
      ) 
}}
export default withStreamlitConnection(MyComponent)
