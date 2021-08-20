/** @jsx jsx */
import * as React from "react"
import { jsx, css } from "@emotion/react"

import FilledButton from "components/atom/filledButton"
import MenuBar from "components/organism/menuBar"

import bgURL from "assets/classroom.png"
import workman from "assets/workman.png"
import logo from "assets/YounGeekLogo.png"

import Header from 'components/organism/header'

const primary = "#F9F871"
const secondary = "#60A8B0"
const tertiary = "#555555"

const Top: React.FC<{}> = () => {
  const heading = css({
    color: primary,
    fontSize: "4vw",
  })
  const subHeading = css({
    color: "white",
    fontSize: "2vw",
    wordWrap: "break-word",
  })
  return (
    //Header,App name(教室の写真のところ)
    <div css={css({
      backgroundColor: `${secondary}`,
      justifyContent: "center",
    })}>
      <MenuBar />
      <div css={css({
        width: "100%",
        height: "calc(100vw*0.48)",
        backgroundImage: `url(${bgURL})`,
        backgroundRepeat: "no-repeat",
        backgroundSize: "contain",

        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
      })}>
        <div
          className="Header"
          css={css({
            width: "100%",
            height: "100%",
            display: "flex",
            justifyContent: "center",
            paddingTop: "120px",
          })}>
          <div css={css({
            width: "80%",
            paddingTop: "4vw"
          })}>
            <div css={css({
              display: "flex",
              flexDirection: "column",
            })}>
              <div css={heading}>先生にも、生徒にも、</div>
              <div css={heading}>"楽"な席替えを。</div>
            </div>
            <div css={css({
              marginTop: "3rem",
            })}>
              <div css={subHeading}>席替え結果は、Excelに出力。</div>
              <div css={subHeading}>簡単な操作で、今すぐ席替えを始めよう。</div>
            </div>
            <div css={css({
              marginTop: "5rem",
            })}>
              <FilledButton text="席替えを始める"/>
            </div>
          </div>
        </div>
        {/*境界線斜め*/}
        <div css={css({
          width: "100%",
          overflow: "hidden",
          lineHeight: "0",
          background: `linear-gradient(45deg, ${secondary} 0%, ${secondary} 50%, rgba(0,0,0,0) 50%,rgba(0,0,0,0) 100%)`,
          bottom: "0",
          height: "150px",
        })}>
        </div>
      </div>

      {/*What's this?*/}
      <div css={css({
        width: "100%",
        marginBlock: "3rem",
        display: "flex",
        justifyContent: "center",
      })}>
        <div css={css({
          width: "80%",

          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between"
        })}>
          <div css={css({
            borderLeft: `solid 10px ${primary}`,
            paddingLeft: "2rem",
            marginBottom: "1rem"
          })}>
            <div css={css({
              color: "white",
              fontSize: "5vw"
            })}>What's this?</div>
          </div>
          <div css={css({
            width: "100%",
            height: "500px",
            display: "flex",
            alignItems: "center",
            background: "rgba(255,255,255,0.25)",
            boxShadow: "2px 2px 4px rgba(0,0,0,0.25)",
            borderRadius: "16px",
          })}>
            <div css={css({
              height: "80%",
              display: "flex",
              flexDirection: "column",
              justifyContent: "space-around",
              paddingLeft: "min(10%,100px)",
            })}>
              <p css={subHeading}>その多くは先生がくじ引きで決めて、</p>
              <p css={subHeading}>クラス委員がノートにまとめる、席替え。</p>
              <p css={subHeading}>[App name]はそんな席替えを、生徒も、先生も、</p>
              <p css={subHeading}>楽しく・ラク(簡単)に行うことができるサービスです。</p>
            </div>
            <img src={workman} alt="teacher who is happy" css={css({
              width: "400px",
              height: "400px",
            })} />
          </div>
        </div>
      </div>

      {/*Features*/}
      <div css={css({
        width: "100%",
        marginBlock: "3rem",
        display: "flex",
        justifyContent: "center",
      })}>
        <div css={css({
          width: "80%",

          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between"
        })}>
          <div css={css({
            borderLeft: `solid 10px ${primary}`,
            paddingLeft: "2rem",
            marginBottom: "1rem"
          })}>
            <div css={css({
              color: "white",
              fontSize: "5vw"
            })}>Features</div>
          </div>
          <div css={css({
            width: "100%",
            height: "500px",
            display: "flex",
            background: "rgba(255,255,255,0.25)",
            boxShadow: "2px 2px 4px rgba(0,0,0,0.25)",
            borderRadius: "16px",
          })}>
            <div css={css({
              display: "flex",
              flexDirection: "column",
              justifyContent: "space-around",
              paddingLeft: "min(10%,100px)",
            })}>
              <div>
                <p css={subHeading}> 1. いびつな形の座席に対応</p>
                <div css={css({
                  marginLeft: "2rem"
                })}><p css={subHeading}>    ロッカーや柱などで机が正方形に並んでいない場合でも利用可能</p></div>
              </div>

              <div>
                <p css={subHeading}> 2. 前席の指定が可能</p>
                <div css={css({
                  marginLeft: "2rem"
                })}><p css={subHeading}>    黒板が見えづらい人がいても安心</p></div>
              </div>

              <div>
                <p css={subHeading}> 3. 席替え結果はExcelに出力</p>
                <div css={css({
                  marginLeft: "2rem"
                })}><p css={subHeading}>    いちいちノートにまとめる必要はありません</p></div>
              </div>

            </div>
          </div>
        </div>
      </div>
      {/*境界線斜め*/}
      <div css={css({
        width: "100%",
        overflow: "hidden",
        lineHeight: "0",
        background: `linear-gradient(45deg, ${primary} 0%, ${primary} 50%, rgba(0,0,0,0) 50%,rgba(0,0,0,0) 100%)`,
        bottom: "0",
        height: "150px",
      })}>
      </div>

      {/*"楽な席替え"を、今すぐ。*/}
      <div css={css({
        width: "100%",
        height: "70vh",
        backgroundColor: `${primary}`,

        display: "flex",
        justifyContent: "center",
      })}>
        <div css={css({
          width: "auto",
          display: "flex",
          flexDirection: "column",
          textAlign: "center",
          justifyContent: "center"
        })}>
          <p css={css({
            color: "black",
            fontSize: "3vw",
            marginBottom: "2rem",
          })}>"楽な席替え"を、今すぐ。</p>
          <div css={css({
            margin: "0 auto",
          })}>
            <FilledButton text="席替えを始める"/>
          </div>
        </div>
      </div>

      {/*境界線斜め*/}
      <div css={css({
        width: "100%",
        overflow: "hidden",
        lineHeight: "0",
        background: `linear-gradient(45deg, ${tertiary} 0%, ${tertiary} 50%, ${primary} 50%,${primary} 100%)`,
        bottom: "0",
        height: "150px",
      })}>
      </div>

      {/*Footer*/}
      <div css={css({
        width: "100%",
        height: "375px",
        backgroundColor: "#555555",

        display: "flex",
        flexDirection: "column",
        justifyContent: "left"
      })}>
        <div css={css({
          paddingLeft: "2rem",
        })}>
          <div css={css({
            width: "80vw",
            display: "flex",
          })}>
            <img css={css({
              width: "100px",
              height: "100px",
              marginRight: "2rem",
            })}
              src={logo}
              alt="YounGeekLogo" />
            <p css={heading}>YounGeek</p>
          </div>
          <div css={css({ width: "80vw" })}><div css={subHeading}>YounGeekは高専生で構成されたWebエンジニアSlackコミュニティです。</div></div>
          <div css={css({
            width: "80vw",
            display: "flex",
            flexDirection: "column",
            marginTop: "2rem",
          })}>
            <div css={subHeading}>coming soon...</div>
            <div css={css({
              display: "flex",
              width: "200px",
              marginTop: "1rem",
            })}>
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" className="bi bi-twitter" viewBox="0 0 16 16">
                <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z" />
              </svg>
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" className="bi bi-facebook" viewBox="0 0 16 16">
                <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z" />
              </svg>
            </div>
          </div>
        </div>
      </div>
      <Header/>
    </div>
  )
}

export default Top