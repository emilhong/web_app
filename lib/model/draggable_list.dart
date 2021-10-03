class DraggableList {
  final String header;
  final List<DraggableListItem> items;
  final index;

  const DraggableList({required this.header, required this.items, this.index});
}

class DraggableListItem {
  final String title;

  const DraggableListItem({
    required this.title,
  });
}
