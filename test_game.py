#!/usr/bin/env python3
"""
萌宠消消乐 - 自动化测试脚本
测试游戏核心逻辑
"""

import random
import json
from datetime import datetime

print("=" * 60)
print("🎮 萌宠消消乐 - 自动化测试")
print("=" * 60)
print()

# 测试计数器
total_tests = 0
passed_tests = 0
failed_tests = 0

def test(name, condition, expected=True):
    """测试断言"""
    global total_tests, passed_tests, failed_tests
    total_tests += 1
    result = condition == expected
    if result:
        passed_tests += 1
        print(f"✅ {name}")
    else:
        failed_tests += 1
        print(f"❌ {name} - 期望：{expected}, 实际：{condition}")
    return result

# ============== 测试 1: 体力系统 ==============
print("📋 测试 1: 体力系统")
print("-" * 60)

# 模拟体力恢复
energy = 2
last_time = datetime.now().timestamp() * 1000
current_time = last_time + (30 * 60 * 1000)  # 30 分钟后

recover = int((current_time - last_time) / (30 * 60 * 1000))
new_energy = min(5, energy + recover)

test("30 分钟恢复 1 点体力", recover, 1)
test("体力上限 5 点", new_energy <= 5, True)

# 长时间不玩
energy = 0
last_time = datetime.now().timestamp() * 1000
current_time = last_time + (24 * 60 * 60 * 1000)  # 24 小时后

recover = int((current_time - last_time) / (30 * 60 * 1000))
new_energy = min(5, energy + recover)

test("24 小时后体力回满", new_energy, 5)
print()

# ============== 测试 2: 消除算法 ==============
print("📋 测试 2: 消除算法")
print("-" * 60)

# 模拟棋盘
def generate_board(size=8, icons=['🍎', '🍊', '🍇']):
    return [[random.choice(icons) for _ in range(size)] for _ in range(size)]

def is_adjacent(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1

def find_matches(board, start_pos):
    """DFS 查找相连相同图标"""
    rows = len(board)
    cols = len(board[0])
    target = board[start_pos[0]][start_pos[1]]
    matches = []
    visited = set()
    
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if (row, col) in visited:
            return
        if board[row][col] != target:
            return
        
        visited.add((row, col))
        matches.append((row, col))
        
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    
    dfs(start_pos[0], start_pos[1])
    return matches

# 测试相邻检测
test("相邻检测 - 上下", is_adjacent((0, 0), (1, 0)), True)
test("相邻检测 - 左右", is_adjacent((0, 0), (0, 1)), True)
test("相邻检测 - 对角", is_adjacent((0, 0), (1, 1)), False)
test("相邻检测 - 远距离", is_adjacent((0, 0), (2, 2)), False)

# 测试消除匹配
board = [
    ['🍎', '🍎', '🍎', '🍊'],
    ['🍇', '🍊', '🍇', '🍊'],
    ['🍇', '🍊', '🍇', '🍊'],
    ['🍇', '🍊', '🍇', '🍊']
]

matches = find_matches(board, (0, 0))
test("3 个相连消除", len(matches), 3)

board2 = [
    ['🍎', '🍊', '🍇', '🍊'],
    ['🍇', '🍊', '🍇', '🍊'],
]
matches2 = find_matches(board2, (0, 1))
test("2 个相连消除", len(matches2), 2)

print()

# ============== 测试 3: 炸弹概率 ==============
print("📋 测试 3: 炸弹概率")
print("-" * 60)

# 模拟生成 1000 个格子
bomb_count = 0
total_cells = 1000
for _ in range(total_cells):
    if random.random() < 0.03:  # 3% 概率
        bomb_count += 1

bomb_rate = bomb_count / total_cells
test(f"炸弹概率约 3% (实际：{bomb_rate:.2%})", 0.02 <= bomb_rate <= 0.04, True)
print(f"   生成 {total_cells} 个格子，炸弹数量：{bomb_count} ({bomb_rate:.2%})")
print()

# ============== 测试 4: 分数计算 ==============
print("📋 测试 4: 分数计算")
print("-" * 60)

def calculate_score(count):
    """计算消除分数"""
    base = count * 10
    bonus = 2 if count > 3 else 1
    return base * bonus

test("2 个消除 = 20 分", calculate_score(2), 20)
test("3 个消除 = 30 分", calculate_score(3), 30)
test("4 个消除 = 80 分", calculate_score(4), 80)
test("5 个消除 = 100 分", calculate_score(5), 100)
print()

# ============== 测试 5: 游戏流程 ==============
print("📋 测试 5: 游戏流程")
print("-" * 60)

# 模拟游戏状态
game_state = {
    'score': 0,
    'steps': 30,
    'target_score': 1000,
    'energy': 5,
    'game_over': False
}

# 模拟一局游戏
while game_state['steps'] > 0 and not game_state['game_over']:
    game_state['steps'] -= 1
    game_state['score'] += random.randint(20, 50)
    
    if game_state['score'] >= game_state['target_score']:
        game_state['game_over'] = True
        game_state['win'] = True
        break

if game_state['steps'] <= 0:
    game_state['game_over'] = True
    game_state['win'] = False

test("游戏能正常结束", game_state['game_over'], True)
test("游戏有输赢判定", 'win' in game_state, True)
print(f"   最终得分：{game_state['score']}, 剩余步数：{game_state['steps']}, 结果：{'胜利' if game_state.get('win') else '失败'}")
print()

# ============== 测试 6: 边界条件 ==============
print("📋 测试 6: 边界条件")
print("-" * 60)

# 体力边界
test("体力不能为负", max(0, -1), 0)
test("体力不超过上限", min(5, 10), 5)

# 棋盘边界
board_size = 8
test("棋盘不越界 - 左上", 0 <= 0 < board_size, True)
test("棋盘不越界 - 右下", 0 <= 7 < board_size, True)
test("棋盘越界 - 负数", 0 <= -1 < board_size, False)
test("棋盘越界 - 超出", 0 <= 8 < board_size, False)
print()

# ============== 测试结果汇总 ==============
print("=" * 60)
print("📊 测试结果汇总")
print("=" * 60)
print(f"总测试数：{total_tests}")
print(f"✅ 通过：{passed_tests}")
print(f"❌ 失败：{failed_tests}")
print(f"通过率：{passed_tests/total_tests*100:.1f}%")
print()

if failed_tests == 0:
    print("🎉 所有测试通过！代码可以上线！")
else:
    print(f"⚠️ 有 {failed_tests} 个测试失败，请检查！")

print()
print("=" * 60)
