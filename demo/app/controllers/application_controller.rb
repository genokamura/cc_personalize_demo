class ApplicationController < ActionController::Base
  def home
  end

  def getRecommend
    arn_prefix = ENV['ARN_PREFIX']

    client = Aws::PersonalizeRuntime::Client.new(
      access_key_id: ENV['AWS_ACCESS_KEY_ID'],
      secret_access_key: ENV['AWS_SECRET_ACCESS_KEY']
    )

    @id = params[:user_id]
    @size = params[:size]
    @recommender = params[:recommender].to_i
    recommender_arn = ENV['ARN_PREFIX']

    if @recommender == 0
      recommender_arn += ENV['BEST_SELLERS']
    else
      recommender_arn += ENV['RECOMMEND_FOR_YOU']
    end

    response = client.get_recommendations({
      user_id: @id,
      num_results: @size,
      recommender_arn: recommender_arn
    })

    @res = response[:item_list]
  end
end

