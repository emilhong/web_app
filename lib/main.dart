import 'package:flutter/material.dart';
import 'package:web_app/data/list_data.dart';
import 'package:web_app/layout/adaptive.dart';
import 'package:drag_and_drop_lists/drag_and_drop_lists.dart';
import 'package:web_app/model/draggable_list.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Todo Web App',
      theme: ThemeData(
          primarySwatch: Colors.blue,
          primaryColor: Colors.blue[600],
          splashColor: Colors.blueAccent,
          iconTheme: IconThemeData(color: Colors.grey)),
      home: MyHomePage(title: 'Project Management'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late List<DragAndDropList> lists;
  // ignore: avoid_init_to_null
  Future? _func = null;
  late TextEditingController addController, totalController;
  List<TextEditingController> controller = [];

  @override
  void initState() {
    super.initState();
    controller = List.generate(allLists.length, (i) => TextEditingController());
    lists = allLists.map(buildList).toList();
    this.addController = TextEditingController();
    this.totalController = TextEditingController();
    // woController.addListener(_onSearchChanged);
    // skuController.addListener(_onSearchChanged);
  }

  @override
  void dispose() {
    // _outputController.removeListener(_onSearchChanged);
    // _itemController.removeListener(_onSearchChanged);
    // _outputController.dispose();
    // _itemController.dispose();
    // _timer?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final isDesktop = isDisplayDesktop(context);
    final body = FutureBuilder(
      future: _func,
      builder: (context, snapshot) {
        if (!snapshot.hasData) {
          return Container(
            constraints: BoxConstraints.expand(),
            padding: const EdgeInsets.all(20.0),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              verticalDirection: VerticalDirection.down,
              children: <Widget>[
                Container(
                  alignment: Alignment.centerLeft,
                  child: Padding(
                    padding: isDesktop
                        ? EdgeInsets.symmetric(horizontal: 5, vertical: 5)
                        : EdgeInsets.symmetric(horizontal: 0, vertical: 0),
                  ),
                ),
                Container(
                  child: headerSection(context),
                ),
                Container(
                  height: MediaQuery.of(context).size.height - 200,
                  child: listSection(context),
                ),
              ],
            ),
          );
        } else {
          return Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[CircularProgressIndicator(), SizedBox(height: 20), Text("wait loading...")],
            ),
          );
        }
      },
    );

    if (isDesktop) {
      return Row(
        children: [
          const VerticalDivider(width: 1),
          Expanded(
              child: Scaffold(
            resizeToAvoidBottomInset: false,
            appBar: AppBar(
              title: Text(widget.title),
            ),
            body: body,
          ))
        ],
      );
    } else {
      return Scaffold(
        resizeToAvoidBottomInset: false,
        appBar: AppBar(
          title: Text(widget.title),
        ),
        body: body,
      );
    }
  }

  headerSection(context) {
    return Container(
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Container(
            width: 250,
            child: Row(
              children: <Widget>[
                Expanded(
                    child: Text('Add project:', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold))),
                Expanded(
                  child: Container(
                    height: 30,
                    child: TextField(
                      onSubmitted: (value) {
                        var str = controller[0].text.replaceAll(new RegExp(r'[^0-9]'), '');
                        setState(() {
                          lists[0].children.insert(
                              int.parse(str),
                              DragAndDropItem(
                                child: ListTile(
                                  title: Text(value),
                                ),
                              ));
                        });
                        addController.text = "";
                      },
                      textInputAction: TextInputAction.search,
                      controller: addController,
                      decoration: InputDecoration(
                        contentPadding: EdgeInsets.all(5.0),
                        border: OutlineInputBorder(borderSide: BorderSide(color: Colors.black)),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
          Container(
            width: 90,
            child: Column(
              children: <Widget>[
                Container(child: Text('TOTAL', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold))),
                Container(
                  height: 60,
                  child: TextField(
                    textAlign: TextAlign.center,
                    maxLines: null,
                    readOnly: true,
                    controller: totalController,
                    decoration: InputDecoration(
                      contentPadding: EdgeInsets.all(5.0),
                      border: OutlineInputBorder(borderSide: BorderSide(color: Colors.black)),
                    ),
                  ),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }

  listSection(context) {
    final isDesktop = isDisplayDesktop(context);
    var total = 0;
    for (int index = 0; index < lists.length; index++) {
      controller[index].text = lists[index].children.length.toString() + ' PROJECT';
      total = total + lists[index].children.length;
    }
    totalController.text = total.toString() + " PROJECT";
    return DragAndDropLists(
      axis: isDesktop ? Axis.horizontal : Axis.vertical,
      listWidth: isDesktop ? MediaQuery.of(context).size.width / 3.5 : double.infinity,
      // listDraggingWidth: ,
      listPadding: EdgeInsets.all(16),
      listInnerDecoration: BoxDecoration(color: Colors.grey[200]),
      children: lists,
      itemDivider: Divider(
        thickness: 2,
        height: 2,
        color: Colors.white,
      ),
      itemDragHandle: buildDragHandle(),
      onItemReorder: onReorderListItem,
      onListReorder: onReorderList,
    );
  }

  DragHandle buildDragHandle({bool isList = false}) {
    final verticalAlignment = isList ? DragHandleVerticalAlignment.top : DragHandleVerticalAlignment.center;
    final color = isList ? Colors.blueGrey : Colors.black26;

    return DragHandle(
      verticalAlignment: verticalAlignment,
      child: Container(
        padding: EdgeInsets.only(right: 10),
        child: Icon(
          Icons.menu,
          color: color,
        ),
      ),
    );
  }

  DragAndDropList buildList(DraggableList list) => DragAndDropList(
        header: Container(
          height: 60,
          decoration: BoxDecoration(color: Colors.grey[600]),
          alignment: Alignment.center,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(
                list.header,
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
              ),
              SizedBox(
                width: 10,
              ),
              Container(
                height: 50,
                width: 90,
                child: TextField(
                  textAlign: TextAlign.center,
                  maxLines: null,
                  readOnly: true,
                  controller: controller[list.index],
                  decoration: InputDecoration(
                    fillColor: Colors.white,
                    filled: true,
                    contentPadding: EdgeInsets.all(5.0),
                    border: OutlineInputBorder(borderSide: BorderSide(color: Colors.white)),
                  ),
                ),
              ),
            ],
          ),
        ),
        children: list.items
            .map(
              (item) => DragAndDropItem(
                child: ListTile(
                  title: Text(item.title),
                ),
              ),
            )
            .toList(),
      );
  void onReorderListItem(
    int oldItemIndex,
    int oldListIndex,
    int newItemIndex,
    int newListIndex,
  ) {
    setState(() {
      final oldListItems = lists[oldListIndex].children;
      final newListItems = lists[newListIndex].children;
      final movedItem = oldListItems.removeAt(oldItemIndex);
      newListItems.insert(newItemIndex, movedItem);
    });
  }

  void onReorderList(
    int oldListIndex,
    int newListIndex,
  ) {
    setState(() {
      final movedList = lists.removeAt(oldListIndex);
      lists.insert(newListIndex, movedList);
    });
  }
}
