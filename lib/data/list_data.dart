import 'package:web_app/model/draggable_list.dart';

List<DraggableList> allLists = [
  DraggableList(header: "To Do", index: 0, items: [
    DraggableListItem(title: "project 1"),
    DraggableListItem(title: "project 2"),
    DraggableListItem(title: "project 3"),
    DraggableListItem(title: "project 4"),
  ]),
  DraggableList(header: "In Progress", index: 1, items: [
    DraggableListItem(title: "project 5"),
    DraggableListItem(title: "project 6"),
    DraggableListItem(title: "project 7"),
  ]),
  DraggableList(header: "Done", index: 2, items: [
    DraggableListItem(title: "project 8"),
    DraggableListItem(title: "project 9"),
    DraggableListItem(title: "project 10"),
    DraggableListItem(title: "project 11"),
    DraggableListItem(title: "project 12"),
  ])
];
