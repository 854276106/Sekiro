import unreal

# 指定你想要遍历的文件夹路径
folder_path = '/Game/Characters/xianyilang/Animations'

# 获取文件夹中的所有资产
assets = unreal.EditorAssetLibrary.list_assets(folder_path)

# 遍历所有资产
for asset_path in assets:
    # 加载每一个资产
    asset = unreal.EditorAssetLibrary.load_asset(asset_path)

    # 检查资产是否是动画序列
    if isinstance(asset, unreal.AnimSequence):
        # 获取动画的导入设置
        import_settings = asset.get_asset_import_data()

        # 检查导入设置是否存在
        if import_settings:
            # 启用根运动
            import_settings.bEnableRootMotion = True

            # 将更改的设置应用到动画序列
            asset.set_asset_import_data(import_settings)

            # 保存更改
            unreal.EditorAssetLibrary.save_loaded_asset(asset)

print("Root motion enabled for all animations in folder.")