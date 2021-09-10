import React, { useEffect, useState } from "react"

import { css } from "@emotion/react"

import firebase from "firebase"
require("firebase/auth")
import $ from "jquery"

import FilledButton from "components/atom/FilledButton"
import LineButton from "components/atom/LineButton"

const firebaseConfig = {
  apiKey: "AIzaSyAbxRa7smokqDD8jeBzqlcH18oPiyK53Ns",
  authDomain: "sekigaeservice.firebaseapp.com",
  projectId: "sekigaeservice",
  storageBucket: "sekigaeservice.appspot.com",
  messagingSenderId: "495374335307",
  appId: "1:495374335307:web:a552c2bdf679edc6547cce",
  measurementId: "G-SZZ1X0Y38Y"
};
firebase.initializeApp(firebaseConfig);

function djangoSignout(): void {
  $.ajax({
    url: "signout",
    type: 'POST',
  }).done((response: string) => {
    window.location.href = response
  })
}

function csrfSafeMethod(method: string) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}

function getCookie(name: string): string {
  var cookieValue: string = ""
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";")
    for (var i = 0; i < cookies.length; i++) {
      var cookie = $.trim(cookies[i])
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue;
}

function authorizationObj(idToken: string) {
  return { "Authorization": `Bearer ${idToken}` }
}

function djangoLogin(idToken: string) {
  const url = "/signin-callback";
  const headers = Object.assign(authorizationObj(idToken))
  $.ajax({
    url: url,
    type: 'POST',
    headers: headers
  }).done((response) => {
    window.location.href = response;
  })
}

const Header: React.FC = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [userName, setUserName] = useState("")

  useEffect(() => {
    firebase.auth().onAuthStateChanged(user => {
      if (user?.displayName) {
        setIsLoggedIn(true)
        setUserName(user.displayName)
      } else {
        setIsLoggedIn(false)
      }
    });

    const csrftoken = getCookie('csrftoken')

    $.ajaxSetup({
      crossDomain: false, // obviates need for sameOrigin test
      beforeSend: function (xhr, settings) {
        //@ts-ignore
        if (!csrfSafeMethod(settings.type)) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken)
        }
      }
    })
  })

  function signIn() {
    const provider = new firebase.auth.GoogleAuthProvider()
    firebase.auth()
      .signInWithPopup(provider)
      .then(async (result) => {
        //@ts-ignore
        const idToken = await firebase.auth().currentUser.getIdToken(true)
        djangoLogin(idToken)
        //@ts-ignore
        setUserName(result.user.displayName)
      }).catch((error) => {
        console.log("エラーコード:" + error.code)
        console.log(error.message)
      })
  }
  function signOut() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          djangoSignout()
          location.reload()
        })
        .catch((error) => {
          console.log(`ログアウト時にエラーが発生しました (${error})`)
        })
  }

  return (
    <div css={css({
      width: "100%",
      height: "100px",
      backgroundColor: "#555555",
      margin: "0 auto",
      display: "flex",
      justifyContent: "space-between",
    })}>
      <h3 css={css({
        color: "white",
        fontSize: "min(5vw,80px)",
        lineHeight: "80px",
        marginLeft: "2rem",
      })}>App name</h3>
      <div css={css({
        display: "flex",
        alignItems: "center"
      })}>
        {isLoggedIn &&
          <div css={css({
            display: "flex",
            alignItems: "center",
          })}>
            <div css={css({
              display: "flex",
            })}>
              <p css={css({
                color: "white",
                fontSize: "18px",
                lineHeight: "50px",
              })}>{userName}としてログインしています</p>
            </div>
            <div css={css({
              marginInline: "2rem",
            })}>
              <LineButton onClick={signOut}>sign out</LineButton>
            </div>
          </div>
        }
        {!isLoggedIn &&
          <div css={css({
            display: "flex",
            paddingBlock: "auto 0",
            alignItems: "center",
            justifyContent: "center",
            marginInline: "2rem",
          })}>
            <FilledButton onClick={signIn}>sign in</FilledButton>
          </div>
        }
      </div>
    </div>
  )
}

export default Header