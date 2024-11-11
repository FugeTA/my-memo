import hou

# 値変更
hou.selectedItems()[0].parm('パラメータ名').set(int)
# 値確認
hou.selectedItems()[0].parm('パラメータ名').eval()

# ノードを指定して値変更
hou.node('/stage/materiallibrary1/karmamaterial/mtlximage1').parmTuple('default_color3').set([0,1,0])
# ノードを指定して値確認
hou.node('/stage/materiallibrary1/karmamaterial/mtlximage1').parmTuple('default_color3').eval()

# 現在開いているネットワークエディター上の階層を取得
net_editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
hou.node(net_editor.currentNode().path()).createNode('subnet','karmamaterial')
print net_editor.currentNode().path()
# networkが複数ある場合はpaneTabOfType('',int)で制御できるが、外部からの判断は不可能おそらく古い順？

# 短縮版
h= hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
print(h.pwd().path())

↓
for i in 
h= hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
net = h.pwd().path()
if not 'obj' in net:
  
# ノード作成
hou.node().createNode('subnet','karmamaterial')

# 複合ノードはこのやり方では作成できない
hou.node("/stage/materiallibrary1").createNode("karmamaterial")

