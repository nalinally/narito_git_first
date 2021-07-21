# narito_git_first
なりとのGit入門

### このリポジトリについて
- パブリックの設定なので、作成者以外でも見れちゃうし、ダウンロード(クローン)できる。
- しかし、許可してないので更新することはできない。
- RasPiで練習してみて

### 使うコマンド
<このリポジトリで練習>
1. ダウンロード(クローン)
git clone https://github.com/Yokohide0317/narito_git_first.git


<なりと用のリポジトリで>
1. GitHubでリポジトリを作成する
本当はPrivateが良いけど、練習だからPublicでいいよ。
作成するときに、「Readmeを追加しますか？」みたいなのがあるから追加しておいて。

2. ダウンロード(クローン)
作成したら、右の『clone』っていうボタンから、URLをコピーして下をコマンドをRasPiで実行
git clone [URL]

3. クローンしたフォルダ内に適当にファイル作成
ls
cd [New_Dirctory]
nano first.txt
とか適当にやって

4. 更新→gitへプッシュ
git add .
git commit -m "message"
git push

ここで、git config --global とかなんとか言われると思う。
コピペして、メールアドレスとGitのユーザーネームを入力して、
もう一度 git pushしたら行ける

5. GitHubで確認
GitHubでラズパイ上のフォルダ内と同期してるか確認！終了！
