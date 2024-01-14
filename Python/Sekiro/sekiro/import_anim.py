import os
import unreal

# 指定要导入动画的源文件夹和导入到UE中的目标文件夹
source_folder = 'E:\\Asset\\xianyilang\\OutFbxAnimation'
target_folder = '/Game/Characters/xianyilang/Animations'

# 创建导入任务
import_task = unreal.AssetImportTask()
import_task.automated = True
import_task.replace_existing = True
import_task.save = True

# 创建导入动画设置
anim_import_settings = unreal.SkeletalMeshImportData()
anim_import_settings.bImportAnimations = True
anim_import_settings.bEnableRootMotion = True
anim_import_settings.bPreserveLocalTransform = True

# 遍历源文件夹中的所有FBX文件
for filename in os.listdir(source_folder):
    if filename.endswith('.fbx'):
        # 设置导入任务的源文件和目标路径
        import_task.filename = os.path.join(source_folder, filename)
        import_task.destination_path = target_folder

        # 设置导入任务的动画导入设置
        import_task.options = anim_import_settings

        # 执行导入任务
        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])

print("Animations imported with root motion enabled.")