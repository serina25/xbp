# coding: utf-8
import text_mining

target_dir = './text_report'

# text_mining.show_conetwork(text_dir=target_dir,
#                            # word="ファッション",
#                            edge_threshold=3,
#                            k=0.7,
#                            sw_list=['こと','とき','もの','ところ','いう','お','しれ','流行っ','人','着る','従兄','言う','時','代','時代','覚える','流行る','今','感じ','思う','当時','ファッション','気','年','頃','行く','あと','買う','かける','記憶','入る','しれる','乗る','始める','後','みる','短大','服','やつ','違う','やる','お父さん','わかる','ごろ','おる','方','売る','忘れる','普通','時期','日本','後半','時期','子','昔','呼ぶ','使う','来る','買える','関する','とる','使える','はやる','20','歳','さっき','着','多かっ','みんな','結構','行っ','系','言っ','覚え','あの','まぁ','入っ','そんな','持っ','ころ','同じ','自分','ちょっと','あんまり','若い','前','まあ','全然','母','友達','買っ','割と','見','まだ','売っ','多く','なんせ','向こう','ずっと','先輩','そー','1','50',])

# text_mining.show_word_rank(text_dir=target_dir,
#                            n_top=40,
#                            sw_list=['こと','とき','もの','ところ','いう','お','しれ','流行っ','人','着る','従兄','言う','時','代','時代','覚える','流行る','今','感じ','思う','当時','ファッション','気','年','頃','行く','あと','買う','かける','記憶','入る','しれる','乗る','始める','後','みる','短大','服','やつ','違う','やる','お父さん','わかる','ごろ','おる','方','売る','忘れる','普通','時期','日本','後半','時期','子','昔','呼ぶ','使う','来る','買える','関する','とる','使える','はやる','20','歳','さっき','着','多かっ','みんな','結構','行っ','系','言っ','覚え','あの','まぁ','入っ','そんな','持っ','ころ','同じ','自分','ちょっと','あんまり','若い','前','まあ','全然','母','友達','買っ','割と','見','まだ','売っ','多く','なんせ','向こう','ずっと','先輩','そー','1','50',],
#                            font_size=3,
#                            bottom_position=0.20)
#
text_mining.show_wordcloud(text_dir=target_dir,
                           sw_list=['こと','とき','もの','ところ','いう','お','しれ','流行っ','人','着る','従兄','言う','時','代','時代','覚える','流行る','今','感じ','思う','当時','ファッション','気','年','頃','行く','あと','買う','かける','記憶','入る','しれる','乗る','始める','後','みる','短大','服','やつ','違う','やる','お父さん','わかる','ごろ','おる','方','売る','忘れる','普通','時期','日本','後半','時期','子','昔','呼ぶ','使う','来る','買える','関する','とる','使える','はやる','20','歳','さっき','着','多かっ','みんな','結構','行っ','系','言っ','覚え','あの','まぁ','入っ','そんな','持っ','ころ','同じ','自分','ちょっと','あんまり','若い','前','まあ','全然','母','友達','買っ','割と','見','まだ','売っ','多く','なんせ','向こう','ずっと','先輩','そー','1','50',],
                           font_path="./fonts/ipaexg.ttf")
