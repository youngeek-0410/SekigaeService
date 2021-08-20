/** @jsx jsx */
import React from "react"
import { jsx } from "@emotion/react"
import { css } from "@emotion/react"

import firebase from "firebase"
require("firebase/auth")
import $ from "jquery"

import FilledButton from "components/atom/filledButton"
import LineButton from "components/atom/lineButton"

const firebaseConfig = {
  apiKey: "AIzaSyAbxRa7smokqDD8jeBzqlcH18oPiyK53Ns",
  authDomain: "sekigaeservice.firebaseapp.com",
  projectId: "sekigaeservice",
  storageBucket: "sekigaeservice.appspot.com",
  messagingSenderId: "495374335307",
  appId: "1:495374335307:web:a552c2bdf679edc6547cce",
  measurementId: "G-SZZ1X0Y38Y"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

interface State {
  isLogined: boolean,
  userName: string
}

class Header extends React.Component<{}, State> {
  constructor(props) {
    super(props)
    this.handleChangeIsLogined = this.handleChangeIsLogined.bind(this)
    this.state = {
      isLogined: false,
      userName: '',
    };
  }

  componentDidMount() {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        this.handleChangeIsLogined(true)
        this.setState({ userName: user.displayName })
      } else {
        this.handleChangeIsLogined(false)
      }
    });

    const csrftoken = this.getCookie('csrftoken');

    $.ajaxSetup({
      crossDomain: false, // obviates need for sameOrigin test
      beforeSend: function (xhr, settings) {
        if (!this.csrfSafeMethod(settings.type)) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });
  }

  handleChangeIsLogined(status) {
    this.setState({ isLogined: status })
  }

  csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = $.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  signIn() {
    window.location.href = "signin"
  }

  djangoSignout() {
    $.ajax({
      url: "signout",
      type: 'POST',
    }).done((response) => {
      window.location.href = response;
    })
  }

  signOut() {
    firebase.auth().onAuthStateChanged(user => {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.djangoSignout();
          location.reload();
        })
        .catch((error) => {
          console.log(`ログアウト時にエラーが発生しました (${error})`);
        });
    });
  }

  render() {
    return (
      <div css={css({
        width:"100%",
        justifyContent:"center",
      })}>
      <div css={css({
        width: "90vw",
        height: "100px",
        backgroundColor: "#555555",
        margin:"0 auto",
        display: "flex",
        justifyContent: "space-between",
      })}>
        <div><h3 css={css({
          color:"white",
          fontSize: "min(5vw,80px)",
          lineHeight: "100px",
        })}>[App name]</h3></div>
        <div css={css({
          display:"flex",
          alignItems:"center"
        })}>
          {this.state.isLogined &&
            <div css={css({
              display: "flex",
              alignItems:"center",
            })}>
              <div css={css({
                display: "flex",
              })}>
                <p css={css({
                  color: "white",
                  fontSize: "18px",
                  lineHeight: "50px",
                })}>{this.state.userName}としてログインしています</p>
              </div>
              <div css={css({
                marginInline:"1rem",
              })}>
              <LineButton text="sign out" onClick={this.signOut} />
              </div>
            </div>
          }
          {!this.state.isLogined &&
            <div css={css({
              display:"flex",
              paddingBlock:"auto 0",
              alignItems:"center",
              justifyContent:"center",
            })}>
            <FilledButton text="sign in" onClick={this.signIn} />
            </div>
          }
        </div>
      </div>
      </div>
    )
  }
}

export default Header