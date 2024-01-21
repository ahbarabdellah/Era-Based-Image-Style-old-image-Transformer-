import 'package:flutter/material.dart';
import 'package:oldpictrans/widgets/camera.dart';

void main() => runApp(ImageTransformerApp());

class ImageTransformerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: ImageTransformerScreen(),
    );
  }
}

class ImageTransformerScreen extends StatefulWidget {
  const ImageTransformerScreen({super.key});

  @override
  State<ImageTransformerScreen> createState() => _ImageTransformerScreenState();
}

class _ImageTransformerScreenState extends State<ImageTransformerScreen> {
  @override
  Widget build(BuildContext context) {
    if (!_controller.value.isInitialized) {
      return Container();
    }
    return Scaffold(
      appBar: AppBar(
        title: Text('Camera Widget'),
      ),
      body: AspectRatio(
        aspectRatio: _controller.value.aspectRatio,
        child: CameraPreview(_controller),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // Take a picture or perform other camera operations here
        },
        child: Icon(Icons.camera_alt),
      ),
    );
  }
}
