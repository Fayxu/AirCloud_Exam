import os


def generate_tree(path: str, depth=0) -> str:
    """
    生成目录树
    :param path: 路径
    :param depth: 递归深度
    :return: structure_tree(str) 目录树
    """
    structure_tree = ""
    if os.path.isdir(path):
        basename = os.path.basename(path)
        structure_tree += f"{'  ' * depth}- **{basename}/**\n"
        for name in sorted(os.listdir(path)):
            structure_tree += generate_tree(os.path.join(path, name), depth + 1)
    else:
        basename = os.path.basename(path)
        structure_tree += f"{'  ' * depth}- {basename}\n"
    return structure_tree


def input_path() -> str:
    path = input("请输入要遍历的根目录：")
    path = path.replace('"', '')  # win11复制文件路径自带双引号
    if not os.path.isdir(path):
        print("输入的根目录不存在，请重新输入")
        path = input_path()
    return path


if __name__ == "__main__":
    root_dir = input_path()  # 指定项目目录
    output_file = os.path.join(root_dir, "README.md")  # 输出文件

    tree = generate_tree(root_dir)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 项目结构\n\n")
        f.write(tree)
    print("项目结构已生成 按任意键退出")
    input()
    os.system("taskkill /f /im cmd.exe")

