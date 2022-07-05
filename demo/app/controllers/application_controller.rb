require_relative './../models/sushi.rb'

class ApplicationController < ActionController::Base
  def home
    # 寿司データを用意
    @items = [
      Sushi.new(0, 'えび', 250),
      Sushi.new(1, '穴子', 350),
      Sushi.new(2, 'まぐろ', 350),
      Sushi.new(3, 'いか', 180),
      Sushi.new(4, 'うに', 600),
      Sushi.new(5, 'いくら', 500),
      Sushi.new(6, '玉子', 130),
      Sushi.new(7, 'とろ', 500),
      Sushi.new(8, '鉄火巻', 350),
      Sushi.new(9, 'かっぱ巻', 180)
    ]

    # AWS接続用情報を用意
    client = Aws::PersonalizeRuntime::Client.new(
      access_key_id: ENV['AWS_ACCESS_KEY_ID'],
      secret_access_key: ENV['AWS_SECRET_ACCESS_KEY'],
      region: ENV['AWS_REGION']
    )


    # ログインボタン押下でユーザIDを特定
    id = params['user_id']

    # ログインボタンが押されていて、かつユーザIDが5000以下であればログイン済み
    @is_logged_in = !id.nil? && id.to_i < 5001

    if @is_logged_in
      @user_name = 'ユーザ' + id
      user_id = id.to_s

      response = client.get_recommendations({
        user_id: user_id,
        num_results: 5,
        recommender_arn: ENV['ARN_PREFIX'] + ENV['RECOMMEND_FOR_YOU']
      })

      @res = response[:item_list]
    end


    res2 = client.get_recommendations({
      user_id: '5001',
      num_results: 5,
      recommender_arn: ENV['ARN_PREFIX'] + ENV['BEST_SELLERS']
    })

    @res2 = res2[:item_list]
  end
end
