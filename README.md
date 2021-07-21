# narito_git_first
なりとのGit入門

### このリポジトリについて
- パブリックの設定なので、作成者以外でも見れちゃうし、ダウンロード(クローン)できる。
- しかし、許可してないので更新することはできない。
- RasPiで練習してみて

### 使うコマンド
<このリポジトリで練習><br>
1. ダウンロード(クローン)<br>
git clone https://github.com/Yokohide0317/narito_git_first.git


<なりと用のリポジトリで>
1. GitHubでリポジトリを作成する<br>
本当はPrivateが良いけど、練習だからPublicでいいよ。<br>
作成するときに、「Readmeを追加しますか？」みたいなのがあるから追加しておいて。

2. ダウンロード(クローン)<br>
作成したら、右の『clone』っていうボタンから、URLをコピーして下をコマンドをRasPiで実行<br>
git clone [URL]

3. クローンしたフォルダ内に適当にファイル作成<br>
ls<br>
cd [New_Dirctory]<br>
nano first.txt<br>
とか適当にやって<br><br>

4. 更新→gitへプッシュ<br>
git add .<br>
git commit -m "変更内容"<br>
git push<br><br>

ここで、git config --global とかなんとか言われると思う。<br>
コピペして、メールアドレスとGitのユーザーネームを入力して、<br>
もう一度 git pushしたら行ける<br>

5. GitHubで確認<br>
GitHubでラズパイ上のフォルダ内と同期してるか確認！終了！<br><br><br>

### 重要なコマンド
- git clone [URL]
- git add .
- git commit -m "変更内容"
- git push

