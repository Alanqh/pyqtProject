/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80031 (8.0.31)
 Source Host           : localhost:3306
 Source Schema         : 动物识别系统

 Target Server Type    : MySQL
 Target Server Version : 80031 (8.0.31)
 File Encoding         : 65001

 Date: 30/03/2023 23:01:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rules
-- ----------------------------
DROP TABLE IF EXISTS `rules`;
CREATE TABLE `rules`  (
  `R_ID` int NOT NULL AUTO_INCREMENT,
  `result` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `conditions` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`R_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 42 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rules
-- ----------------------------
INSERT INTO `rules` VALUES (1, '哺乳动物', '有奶');
INSERT INTO `rules` VALUES (2, '哺乳动物', '有毛发');
INSERT INTO `rules` VALUES (3, '鸟类', '有羽毛');
INSERT INTO `rules` VALUES (4, '鸟类', '会飞/卵生');
INSERT INTO `rules` VALUES (5, '食肉动物', '哺乳动物/有爪/有犬齿/目盯前方');
INSERT INTO `rules` VALUES (6, '食肉动物', '哺乳动物/吃肉');
INSERT INTO `rules` VALUES (7, '有蹄动物', '哺乳动物/有蹄');
INSERT INTO `rules` VALUES (8, '偶蹄动物', '有蹄动物/反刍食物');
INSERT INTO `rules` VALUES (9, '老虎', '食肉动物/黄褐色/有黑色条纹');
INSERT INTO `rules` VALUES (10, '金钱豹', '食肉动物/黄褐色/有黑色斑点');
INSERT INTO `rules` VALUES (11, '长颈鹿', '有蹄动物/长腿/长脖子/黄褐色/有暗斑点');
INSERT INTO `rules` VALUES (12, '斑马', '有蹄动物/白色/有黑色条纹');
INSERT INTO `rules` VALUES (13, '驼鸟', '鸟类/不会飞/长腿/长脖子/黑白色');
INSERT INTO `rules` VALUES (14, '企鹅', '鸟类/不会飞/会游泳/黑白色');
INSERT INTO `rules` VALUES (15, '海燕', '鸟类/会飞/不怕风浪');
INSERT INTO `rules` VALUES (16, '哺乳动物', '有毛发/有奶');
INSERT INTO `rules` VALUES (17, '兔子', '哺乳动物/善跳跃/唇裂');
INSERT INTO `rules` VALUES (18, '猫', '哺乳动物/善捕鼠/脚有肉垫');
INSERT INTO `rules` VALUES (19, '犀牛', '哺乳动物/鼻子上有角/褐色/皮糙肉厚/有蹄');
INSERT INTO `rules` VALUES (20, '熊猫', '哺乳动物/黑眼圈/四肢短小');
INSERT INTO `rules` VALUES (21, '鹦鹉', '鸟类/上嘴鹰钩/会模仿人说话');
INSERT INTO `rules` VALUES (22, '鸭子', '鸟类/腿短/嘴扁平/善潜水游泳');
INSERT INTO `rules` VALUES (23, '鹰', '鸟类/上嘴鹰钩/有爪/吃肉');
INSERT INTO `rules` VALUES (24, '鸟类', '有羽毛/卵生');
INSERT INTO `rules` VALUES (25, '鸭子', '鸟类/会游泳/嘴扁平/腿短');
INSERT INTO `rules` VALUES (26, '鹅', '鸟类/善潜水游泳/白色或黑色/颈长/嘴大/腿长');
INSERT INTO `rules` VALUES (27, '鸦', '鸟类/黑色/嘴大');
INSERT INTO `rules` VALUES (28, '鹰', '鸟类/有爪/吃肉/上嘴鹰钩');
INSERT INTO `rules` VALUES (29, '两栖动物', '卵生/生活在水中/生活在陆地/用皮肤呼吸/用肺呼吸');
INSERT INTO `rules` VALUES (30, '青蛙', '两栖动物/皮肤光滑/吃昆虫');
INSERT INTO `rules` VALUES (31, '蝾螈', '两栖动物/吃昆虫/皮肤光滑/四肢扁/背部黑色');
INSERT INTO `rules` VALUES (32, '蟾蜍', '两栖动物/吃昆虫/皮肤粗糙');
INSERT INTO `rules` VALUES (33, '鱼类', '用鳃呼吸/身体有鳍');
INSERT INTO `rules` VALUES (34, '比目鱼', '鱼类/生活在海洋中/身体扁平/两眼在头部同侧');
INSERT INTO `rules` VALUES (35, '鲫鱼', '鱼类/生活在淡水中/身体扁平/头高尾部窄');
INSERT INTO `rules` VALUES (36, '爬行动物', '生活在陆地/用肺呼吸/胎生/身体有鳞或甲');
INSERT INTO `rules` VALUES (37, '蛇', '爬行动物/身体圆而细长/吃小动物');
INSERT INTO `rules` VALUES (38, '壁虎', '爬行动物/有四肢/尾巴细长易断/吃昆虫');
INSERT INTO `rules` VALUES (39, '乌龟', '爬行动物/身体圆而扁/有坚硬的壳');
INSERT INTO `rules` VALUES (40, '玳瑁', '爬行动物/壳为黄褐色/皮肤光滑/有黑斑');
INSERT INTO `rules` VALUES (41, '鳄鱼', '爬行动物/有四肢/善游泳/皮硬/黑褐色');

SET FOREIGN_KEY_CHECKS = 1;
