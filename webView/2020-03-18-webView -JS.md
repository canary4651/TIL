# WebView에서 JavaScript 실행하기
- React Native(Expo)로 웹 페이지를 띄우고, JavaScript를 실행하는 방법
[공부](https://github.com/ahastudio/til/blob/master/react-native/2020-03-16-webview-inject-javascript.md#instagram-%EA%B0%84%EB%8B%A8-%EB%B6%84%EC%84%9D)

## 목표 : 인스타그램에서 사진만 보여주기
- 제거할 요소들

```js
document.querySelector('nav').remove();
document.querySelector('footer').remove();
document.querySelector('article > header').remove();
document.querySelector('article > div:nth-of-type(3)').remove();
document.querySelector('article > div:nth-of-type(2)').remove();
```

## React Native App 만들기

`instaview`

```git
npx -p expo-cli expo init instaview
```
- blank template 선택
- 프로젝트 폴더로 이동해서 `expo-cli` 의존성 추가
```git
cd instaview

npm install --save-dev expo-cli
```
`webView` 설치
```git
npx expo install react-native-webview
```
Expo Developer Tools를 실행
```git
npm start
```
핸드폰으로 확인 가능 (expo app 설치)

## WebView 띄우기
`App.js` 수정
```js
import React from 'react';
import { WebView } from "react-native-webview";

export default function App() {
  return (
      <WebView
  source={{ uri: 'https://www.instagram.com/p/BprMuMYneO-/' }}
  />
);
}
```
인스타그램 페이지가 나옴

## Java Script Code
```js
import React from 'react';
import { WebView } from "react-native-webview";

const script = `
  document.querySelector('nav').remove();
  document.querySelector('footer').remove();
  document.querySelector('article > header').remove();
  document.querySelector('article > div:nth-of-type(3)').remove();
  document.querySelector('article > div:nth-of-type(2)').remove();
`;

export default function App() {
  return (
      <WebView
  source={{ uri: 'https://www.instagram.com/p/BprMuMYneO-/' }}
  injectedJavaScript={script}
  />
);
}
```

