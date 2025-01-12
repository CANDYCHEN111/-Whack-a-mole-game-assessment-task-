
import pandas as pd
from psychopy import visual, core, event, gui
import time

# 全局变量存储被试信息
subj_info = {}

def getSubjInfo():
    global subj_info  # 声明为全局变量
    subj_info = {"ID": '', 'name': '', 'age': '', "gender": ''}
    infoDlg = gui.DlgFromDict(dictionary=subj_info, title='被试信息', order=['ID', 'name', 'age', 'gender'])
    if not infoDlg.OK:  # 如果对话框被取消
        core.quit()
getSubjInfo()


# 设置窗口
win = visual.Window([800, 600], color="grey", units="pix",fullscr=False)

# 加载背景图片（划分象限的背景图）
background = visual.ImageStim(win, image="D:/HuaweiMoveData/Users/86188/Desktop/实心实验/背景.png", size=[800, 600])

# 加载地鼠图片
mole = visual.ImageStim(win, image="D:/HuaweiMoveData/Users/86188/Desktop/实心实验/地鼠2.webp", size=[100, 100])

# 设置象限的位置
quadrants = [
    [-150, 100], [150, 100],   # 上半部分
    [-150, -100], [150, -100]  # 下半部分
]

# 读取设计矩阵
design_matrix = pd.read_excel("D:/HuaweiMoveData/Users/86188/Desktop/实心实验/design.xlsx", header=0)

# 数据记录
results = []  # 用于存储每次地鼠的出现象限、反应时和是否正确
correct_clicks = 0


# 确保每个象限不会连续出现超过两次
def shuffle_trials(trials):
    shuffled_trials = trials.sample(frac=1).reset_index(drop=True)
    
    # 避免相邻两次出现同一象限三次及以上
    while any(shuffled_trials['quadrants'].iloc[i] == shuffled_trials['quadrants'].iloc[i + 1] == shuffled_trials['quadrants'].iloc[i + 2] for i in range(len(shuffled_trials) - 2)):
        shuffled_trials = trials.sample(frac=1).reset_index(drop=True)
    
    return shuffled_trials

# 检查是否按下 `Esc` 键以退出程序
def check_exit():
    keys = event.getKeys()
    if 'escape' in keys:
        core.quit()

# 显示文字
def put_txt(txt, loc=(0,0),font_size=50,color='black', win=win):
    text_1= visual.TextStim(win, text = txt,
    pos = loc,
    height=font_size,
    color = color,
	bold = True,
    alignHoriz='center',
    alignVert='center',
    wrapWidth=800)
    text_1.draw()
    win.flip()


def instructions(MODE):
	#Presenting the instructions
    if MODE == 'prac':
        put_txt("现在请您练习下。\n\n请在地鼠出现后进快点击地鼠。\n\n明白后，按空格键开始\n\n实验中可随时使用Esc退出", (0,0))
        event.waitKeys(keyList =['space'])
    if MODE == 'formal_1': 
        put_txt("现在开始正式实验第一关。\n\n请在地鼠出现后进快点击地鼠。\n\n明白后，按空格键开始", (0,0))
        event.waitKeys(keyList =['space'])
    if MODE == 'formal_2': 
        put_txt("现在开始正式实验第二关。\n\n请在地鼠出现后进快点击地鼠。\n\n明白后，按空格键开始", (0,0))
        event.waitKeys(keyList =['space'])
    if MODE == 'end': 
        put_txt("按空格结束，谢谢参与！", (0,0))
        event.waitKeys(keyList =['space'])
    if MODE == 'rest': 
        put_txt("请您至少休息30秒。\n\n之后可以按空格键开始下一关。", (0,0))
        event.waitKeys(keyList =['space'])


# 练习阶段
def run_practice_block():
    global results, correct_clicks
    trials_completed = 0
    # 练习阶段读取前40行并打乱
    practice_trials = shuffle_trials(design_matrix.iloc[:40])  # 打乱顺序
    while trials_completed < len(practice_trials):
        check_exit()  # 检查是否按下 `Esc` 键

        # 获取当前trial的象限和呈现时间
        trial_data = practice_trials.iloc[trials_completed]
        quadrant = trial_data['quadrants'] - 1  # 将象限1-4转换为索引0-3
        display_time = trial_data['time'] / 1000  # 转换为秒

        # 获取象限位置
        loc = quadrants[quadrant]
        mole.setPos(loc)

        # 显示背景和地鼠
        background.draw()
        mole.setAutoDraw(True)
        win.flip()  # 确保背景和地鼠被绘制到屏幕上
        start_time = time.time()

        # 等待玩家点击
        mouse = event.Mouse()
        mouse.setPos([0, 0])
        clicked = False
        click_time = None  # 用于存储点击时间
        while time.time() - start_time < display_time:  # 地鼠至少显示到设计矩阵中的时间
            check_exit()  # 检查是否按下 `Esc` 键

            if mouse.isPressedIn(mole):  # 点击地鼠
                if not clicked:  # 第一次点击
                    click_time = time.time() - start_time
                    mole.contrast = 0.5  # 点击后地鼠图片变暗
                clicked = True

            background.draw()
            mole.draw()
            win.flip()  # 刷新窗口

        # 计算反应时和记录是否正确
        if clicked:
            reaction_time = click_time
            correct = True
            correct_clicks += 1
        else:
            reaction_time = display_time
            correct = False

        # 保存当前结果
        results.append({
            "Trial": trials_completed + 1,
            "Quadrant": quadrant + 1,
            "Reaction Time (s)": reaction_time,
            "Correct": correct
        })

        trials_completed += 1
        mole.setAutoDraw(False)  # 结束当前的地鼠显示
        mole.contrast = 1.0  # 恢复地鼠图片亮度

# 正式实验阶段
def run_experiment_block(block_number):
    global results, correct_clicks
    trials_completed = 0
    # 根据block选择读取不同的试次并打乱
    if block_number == 1:
        experiment_trials = shuffle_trials(design_matrix.iloc[:40])# block1读取前40行并打乱
    else:
        experiment_trials = shuffle_trials(design_matrix.iloc[40:])  # block2读取后40行并打乱

    while trials_completed < len(experiment_trials):
        check_exit()  # 检查是否按下 `Esc` 键

        # 获取当前trial的象限和呈现时间
        trial_data = experiment_trials.iloc[trials_completed]
        quadrant = trial_data['quadrants'] - 1  # 将象限1-4转换为索引0-3
        display_time = trial_data['time'] / 1000  # 转换为秒

        # 获取象限位置
        loc = quadrants[quadrant]
        mole.setPos(loc)

        # 显示背景和地鼠
        background.draw()
        mole.setAutoDraw(True)
        win.flip()  # 刷新窗口
        start_time = time.time()

        # 等待玩家点击
        mouse = event.Mouse()
        mouse.setPos([0, 0])
        clicked = False
        click_time = None  # 用于存储点击时间
        while time.time() - start_time < display_time:  # 地鼠至少显示到设计矩阵中的时间
            check_exit()  # 检查是否按下 `Esc` 键

            if mouse.isPressedIn(mole):  # 点击地鼠
                if not clicked:  # 第一次点击
                    click_time = time.time() - start_time
                    mole.contrast = 0.5  # 点击后地鼠图片变暗
                clicked = True

            background.draw()
            mole.draw()
            win.flip()  # 刷新窗口

        # 计算反应时和记录是否正确
        if clicked:
            reaction_time = click_time
            correct = True
            correct_clicks += 1
        else:
            reaction_time = display_time
            correct = False

        # 保存当前结果
        results.append({
            "Trial": trials_completed + 1,
            "Quadrant": quadrant + 1,
            "Reaction Time (s)": reaction_time,
            "Correct": correct
        })

        trials_completed += 1
        mole.setAutoDraw(False)  # 结束当前的地鼠显示
        mole.contrast = 1.0  # 恢复地鼠图片亮度



def rest_period():
     # 获取当前时间
    start_time = core.getTime()
    instructions('rest')  # 显示休息的提示
   # 等待至少30秒
    while core.getTime() - start_time < 30:
        if event.getKeys(keyList=['space']):   #检查是否有按键，但不继续
            pass  # 如果有按键，不执行任何操作，继续等待

        # 等待被试按下空格键以继续
    event.waitKeys(keyList=['space'])

    

# 主程序流程
def main():
    try:
        # getSubjInfo()  # 获取被试信息
        # 练习阶段
        instructions('prac')
        run_practice_block()

        # 如果练习通过，则开始正式实验
        if correct_clicks >= 40 * 0.8:  # 练习正确率达到80%进入正式实验
            # 第一个正式实验block
            print("开始第一个正式实验block")
            instructions('formal_1')
            run_experiment_block(1)

            # 休息阶段
            rest_period()

            # 第二个正式实验block
            print("开始第二个正式实验block")
            instructions('formal_2')
            run_experiment_block(2)
            instructions('end')

            print("实验结束")
        else:
            print("练习阶段未达到80%的正确率，无法进入正式实验")
    except Exception as e:
        print(f"实验中发生错误: {e}")

    finally:
        if len(results) > 0:
            results_df = pd.DataFrame(results)

        # 创建新的 DataFrame，将被试信息放在前面
            subj_info_df = pd.DataFrame([subj_info])  # 将被试信息转换为 DataFrame
            final_df = pd.concat([subj_info_df] * len(results_df), ignore_index=True)  # 重复被试信息到每行
            final_df = pd.concat([final_df, results_df], axis=1)  # 合并被试信息和结果数据

        # 动态生成文件名，加入被试 ID
            file_name = f"D:/HuaweiMoveData/Users/86188/Desktop/experiment_results_{subj_info['ID']}.xlsx"

        # 保存结果到 Excel 文件
            final_df.to_excel(file_name, index=False)
            print(f"实验结果已保存到 '{file_name}'")
        else:
            print("未记录任何实验数据，未生成结果文件。")
    
       
# 开始实验  
main()
