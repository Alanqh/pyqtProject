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

 Date: 30/03/2023 23:00:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for features
-- ----------------------------
DROP TABLE IF EXISTS `features`;
CREATE TABLE `features`  (
  `F_ID` int NOT NULL AUTO_INCREMENT,
  `feature` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`F_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 78 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of features
-- ----------------------------
INSERT INTO `features` VALUES (1, '有奶');
INSERT INTO `features` VALUES (2, '有毛发');
INSERT INTO `features` VALUES (3, '有羽毛');
INSERT INTO `features` VALUES (4, '会飞');
INSERT INTO `features` VALUES (5, '卵生');
INSERT INTO `features` VALUES (6, '哺乳动物');
INSERT INTO `features` VALUES (7, '有爪');
INSERT INTO `features` VALUES (8, '有犬齿');
INSERT INTO `features` VALUES (9, '目盯前方');
INSERT INTO `features` VALUES (10, '吃肉');
INSERT INTO `features` VALUES (11, '有蹄');
INSERT INTO `features` VALUES (12, '有蹄动物');
INSERT INTO `features` VALUES (13, '反刍食物');
INSERT INTO `features` VALUES (14, '食肉动物');
INSERT INTO `features` VALUES (15, '黄褐色');
INSERT INTO `features` VALUES (16, '有黑色条纹');
INSERT INTO `features` VALUES (17, '有黑色斑点');
INSERT INTO `features` VALUES (18, '长腿');
INSERT INTO `features` VALUES (19, '长脖子');
INSERT INTO `features` VALUES (20, '有暗斑点');
INSERT INTO `features` VALUES (21, '白色');
INSERT INTO `features` VALUES (22, '鸟类');
INSERT INTO `features` VALUES (23, '不会飞');
INSERT INTO `features` VALUES (24, '黑白色');
INSERT INTO `features` VALUES (25, '会游泳');
INSERT INTO `features` VALUES (26, '不怕风浪');
INSERT INTO `features` VALUES (27, '善跳跃');
INSERT INTO `features` VALUES (28, '唇裂');
INSERT INTO `features` VALUES (29, '善捕鼠');
INSERT INTO `features` VALUES (30, '脚有肉垫');
INSERT INTO `features` VALUES (31, '鼻子上有角');
INSERT INTO `features` VALUES (32, '褐色');
INSERT INTO `features` VALUES (33, '皮糙肉厚');
INSERT INTO `features` VALUES (34, '黑眼圈');
INSERT INTO `features` VALUES (35, '四肢短小');
INSERT INTO `features` VALUES (36, '上嘴鹰钩');
INSERT INTO `features` VALUES (37, '会模仿人说话');
INSERT INTO `features` VALUES (38, '腿短');
INSERT INTO `features` VALUES (39, '嘴扁平');
INSERT INTO `features` VALUES (40, '善潜水游泳');
INSERT INTO `features` VALUES (41, '白色或黑色');
INSERT INTO `features` VALUES (42, '颈长');
INSERT INTO `features` VALUES (43, '嘴大');
INSERT INTO `features` VALUES (44, '腿长');
INSERT INTO `features` VALUES (45, '黑色');
INSERT INTO `features` VALUES (46, '生活在水中');
INSERT INTO `features` VALUES (47, '生活在陆地');
INSERT INTO `features` VALUES (48, '用皮肤呼吸');
INSERT INTO `features` VALUES (49, '用肺呼吸');
INSERT INTO `features` VALUES (50, '两栖动物');
INSERT INTO `features` VALUES (51, '皮肤光滑');
INSERT INTO `features` VALUES (52, '吃昆虫');
INSERT INTO `features` VALUES (53, '皮肤粗糙');
INSERT INTO `features` VALUES (54, '四肢扁');
INSERT INTO `features` VALUES (55, '背部黑色');
INSERT INTO `features` VALUES (56, '用鳃呼吸');
INSERT INTO `features` VALUES (57, '身体有鳍');
INSERT INTO `features` VALUES (58, '鱼类');
INSERT INTO `features` VALUES (59, '生活在海洋中');
INSERT INTO `features` VALUES (60, '身体扁平');
INSERT INTO `features` VALUES (61, '两眼在头部同侧');
INSERT INTO `features` VALUES (62, '生活在淡水中');
INSERT INTO `features` VALUES (63, '头高尾部窄');
INSERT INTO `features` VALUES (64, '胎生');
INSERT INTO `features` VALUES (65, '身体有鳞或甲');
INSERT INTO `features` VALUES (66, '爬行动物');
INSERT INTO `features` VALUES (67, '身体圆而细长');
INSERT INTO `features` VALUES (68, '吃小动物');
INSERT INTO `features` VALUES (69, '有四肢');
INSERT INTO `features` VALUES (70, '尾巴细长易断');
INSERT INTO `features` VALUES (71, '身体圆而扁');
INSERT INTO `features` VALUES (72, '有坚硬的壳');
INSERT INTO `features` VALUES (73, '壳为黄褐色');
INSERT INTO `features` VALUES (74, '有黑斑');
INSERT INTO `features` VALUES (75, '善游泳');
INSERT INTO `features` VALUES (76, '皮硬');
INSERT INTO `features` VALUES (77, '黑褐色');

SET FOREIGN_KEY_CHECKS = 1;
