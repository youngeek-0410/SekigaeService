# Frontend project of SekigaeService

## Rules

### Directory structure
- `pages/` ディレクトリはルーティングのためだけに利用
    - このディレクトリに置かれたファイルは、ルーティングのパスの決定のみに使う
- `src/` ソースコードを置く
    - `page/` 
        - ページをつくる
        - ルーティングのパスとページコンポーネントの命名は違っても構わない
    - `common/`
        - アプリ内で共通のもろもろ
        - モデルに関心がない処理をここに集める
    - `[model]/`
        - モデルに関心のある処理を
        - モデル名をディレクトリ名にする
        - `[model]/components` に配置するコンポーネントは、モデル名のprefixをつける

例
```
- pages/
    - index.tsx
    - about.tsx
- src/
    - page/
        - index.tsx
        - about.tsx
    - common/
        - components/
        - hooks/
        - context/
        - types/
    - [model/]
        - components/
        - hooks/
        - context/
        - types/
    - user/
        - components/
            - UserList.tsx
            - UserDetail.tsx
        - hooks/
        - context/
        - types/
            - User.d.ts
    - company/
        - components/
            - CompanyList.tsx
            - CompanyDetail.tsx
        - hooks/
        - context/
        - types/
            - Company.d.ts
```