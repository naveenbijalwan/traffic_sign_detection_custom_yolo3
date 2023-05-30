import os
import xml.etree.ElementTree as ET

def convert_labelimg_to_yolo(labelimg_folder, output_folder, class_mapping):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(labelimg_folder):
        if filename.endswith(".xml"):
            xml_path = os.path.join(labelimg_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")

            tree = ET.parse(xml_path)
            root = tree.getroot()

            with open(output_path, "w") as f:
                for obj in root.findall("object"):
                    class_name = obj.find("name").text
                    if class_name not in class_mapping:
                        continue

                    class_id = class_mapping[class_name]

                    bndbox = obj.find("bndbox")
                    xmin = float(bndbox.find("xmin").text)
                    ymin = float(bndbox.find("ymin").text)
                    xmax = float(bndbox.find("xmax").text)
                    ymax = float(bndbox.find("ymax").text)

                    # Calculate YOLO format coordinates
                    width = xmax - xmin
                    height = ymax - ymin
                    x_center = xmin + width / 2
                    y_center = ymin + height / 2

                    # Normalize coordinates
                    image_width = int(root.find("size/width").text)
                    image_height = int(root.find("size/height").text)
                    x_center /= image_width
                    y_center /= image_height
                    width /= image_width
                    height /= image_height

                    # Write YOLO annotation to file
                    line = f"{class_id} {x_center} {y_center} {width} {height}\n"
                    f.write(line)

# Usage example
labelimg_folder = "path/to/labelimg/annotations"
output_folder = "path/to/output/folder"
class_mapping = {
    "class1": 0,
    "class2": 1,
    # Add more class mappings as needed
}

convert_labelimg_to_yolo(labelimg_folder, output_folder, class_mapping)