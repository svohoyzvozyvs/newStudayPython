import random

menu = ['川味凤爪','香辣虾','紫花菌炒肉','泡椒肥肠','红乳牛肝菌','拼盘128','油炸花生米','炝炒时蔬','豌豆肉末','猴头菇','水煮肉片','田园大丰收','菌拼168','手撕包菜','手工爆浆豆腐','妈妈蛋卷','如意粉丝煲','蒜台腊肉','干锅鱿鱼须','姬松茸','腊肉炒糯米笋','豇豆肉末','白灼菜心','松菌','辣菜肉沫','砂锅牛腩煲','野葱烩灰豆腐','手抓排骨','樟树港辣椒炒肉','小炒香干','时令杂菌拼88','尖椒木耳','碧波杂粮窝窝头','黔味凉拌猪耳','鲜竹荪','羊肚菌','桂花糕','黔味卤水拼盘','捞汁花甲','生爆猪肝','时令菌拼128','火爆鸡血','黑牛肝菌','乡下腊肉','榕江卷皮','菌拼98','凉拌皮蛋','黔北糟辣肉','柴把鸭子','泡椒牛蛙','鱼湫辣椒','菌拼68','小炒牛肝菌','丝瓜鸡蛋汤','生爆板筋','泡椒鸡杂','铁板土豆片','花甲蒸水蛋','小炒黄牛肉','捞汁秋葵','见手青','特色炝锅鱼','鲜活清蒸多宝鱼','大方宫爆肉','紫花菌','红糖发糕','金耳菌','青笋肉丝','白菜烩小豆','青椒鸡野生菌','青椒肉末烩豆米','丝瓜悶土蛋','鲜活白灼大虾','清汤肉饼土鸡','凉拌折耳根','干锅有机菜花','农村红烧肉','酒仙三宝','农家盐菜肉','白菜粉丝丸子汤','酸菜小豆汤','鲜活清蒸鲈鱼','川渝毛血旺','黔味凉拌牛肉','糟辣鲈鱼','三鲜汤','蒜蓉粉丝蒸扇贝','香辣小酥肉','茄角之恋']


def add_dish():
    """添加菜品"""
    dish_name = input("请输入菜名：")
    menu.append(dish_name)
    print(f"已添加菜品：{dish_name}")


def generate_menu(num_dishes):
    """随机生成菜单"""
    if not menu:
        print("菜单为空，请先添加菜品。")
        return []
    if num_dishes > len(menu):
        print(f"菜品数量不足，最多只能选择 {len(menu)} 个菜品。")
        num_dishes = len(menu)

    selected_dishes = random.sample(menu, num_dishes)
    return selected_dishes


def display_menu(dishes):
    """显示菜单"""
    if not dishes:
        print("没有可显示的菜单。")
        return
    print("今日菜单：")
    for i, dish in enumerate(dishes):
        print(f"{i + 1}. {dish}")


def main():
    while True:
        print("\n请选择操作：")
        print("1. 添加菜品")
        print("2. 生成菜单")
        print("3. 显示所有菜品")
        print("4. 退出")

        choice = input("请输入你的选择：")

        if choice == "1":
            add_dish()
        elif choice == "2":
            num_dishes = int(input("请输入要生成多少个菜品："))
            generated_menu = generate_menu(num_dishes)
            display_menu(generated_menu)
        elif choice == "3":
            display_menu(menu)
        elif choice == "4":
            print("程序已退出。")
            break
        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()
